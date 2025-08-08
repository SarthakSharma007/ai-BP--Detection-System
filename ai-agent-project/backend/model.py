# model.py - AI Logic for Blood Pressure Risk Analysis
import re

def analyze_symptoms(symptoms: str):
    s = symptoms.lower()

    # Extract BP value from input (first number found)
    match = re.search(r'\d+', s)
    bp_value = int(match.group()) if match else None

    # Symptom-based scoring
    highBPSymptoms = {
        'headache': 25, 'severe headache': 35,
        'dizziness': 20, 'dizzy': 20,
        'chest pain': 40, 'tightness': 30,
        'blurred vision': 30, 'vision problems': 30,
        'fatigue': 15, 'tired': 15,
        'shortness of breath': 35, 'breathing difficulty': 35,
        'nosebleed': 25,
        'pounding in chest': 30, 'neck': 20, 'ears': 20,
        'confusion': 25,
    }

    lowBPSymptoms = {
        'dizziness': 25, 'dizzy': 25, 'lightheadedness': 30,
        'fainting': 40, 'syncope': 40,
        'blurred vision': 20,
        'nausea': 20,
        'fatigue': 25, 'weakness': 25,
        'cold skin': 15, 'clammy skin': 15, 'pale skin': 15,
        'rapid breathing': 20, 'shallow breathing': 20,
        'lack of concentration': 20, 'trouble concentrating': 20,
        'thirsty': 15, 'thirst': 15
    }

    highBPRisk = sum(weight for symptom, weight in highBPSymptoms.items() if symptom in s)
    lowBPRisk = sum(weight for symptom, weight in lowBPSymptoms.items() if symptom in s)

    highBPRisk = min(highBPRisk, 100)
    lowBPRisk = min(lowBPRisk, 100)

    highBPTips = [
        "Reduce sodium in your diet.",
        "Engage in regular physical activity.",
        "Limit alcohol consumption.",
        "Manage stress through relaxation techniques.",
        "Monitor your blood pressure at home."
    ]
    
    lowBPTips = [
        "Increase your salt intake slightly, after consulting a doctor.",
        "Drink more water to avoid dehydration.",
        "Wear compression stockings.",
        "Eat small, low-carb meals throughout the day.",
        "Stand up slowly to avoid sudden drops in pressure."
    ]
    
    generalTips = [
        "Maintain a healthy weight.",
        "Eat a balanced diet rich in fruits and vegetables.",
        "Get regular check-ups with your doctor."
    ]

    # ✅ Number-based BP logic first
    if bp_value is not None:
        if bp_value < 90:
            return {
                "text": f"Your BP reading ({bp_value}) suggests low blood pressure.",
                "confidence": 90,
                "tips": lowBPTips
            }
        elif 90 <= bp_value <= 120:
            return {
                "text": f"Your BP reading ({bp_value}) is in the normal range.",
                "confidence": 95,
                "tips": generalTips
            }
        elif 121 <= bp_value <= 139:
            return {
                "text": f"Your BP reading ({bp_value}) suggests pre-hypertension.",
                "confidence": 85,
                "tips": highBPTips
            }
        else:  # bp_value >= 140
            return {
                "text": f"Your BP reading ({bp_value}) suggests high blood pressure.",
                "confidence": 95,
                "tips": highBPTips
            }

    # ✅ Symptom-based logic if no number given
    if highBPRisk > 60 or (highBPRisk > 30 and highBPRisk > lowBPRisk):
        return {
            "text": "You might have a risk of high blood pressure. Please get this checked.",
            "confidence": highBPRisk,
            "tips": highBPTips
        }
    if lowBPRisk > 50 or (lowBPRisk > 30 and lowBPRisk > highBPRisk):
        return {
            "text": "You might have a risk of low blood pressure. Please consult a doctor.",
            "confidence": lowBPRisk,
            "tips": lowBPTips
        }
    if highBPRisk > 20 or lowBPRisk > 20:
        return {
            "text": "Symptoms are mild but should be monitored.",
            "confidence": max(highBPRisk, lowBPRisk) + 10,
            "tips": generalTips
        }
    return {
        "text": "No strong BP symptoms detected. Stay healthy!",
        "confidence": 75,
        "tips": generalTips
    }
