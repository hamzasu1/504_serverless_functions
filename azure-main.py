import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Function.
    Expects JSON with 'fasting_glucose_mg_dL'
    Returns a JSON classification of fasting glucose. Utilizing ada sample ranges
    """
    try:
        data = req.get_json()   
    except ValueError:
        data = {}

    fg = data.get("fasting_glucose_mg_dL") or req.params.get("fasting_glucose_mg_dL")

    if fg is None:
        return func.HttpResponse(
            json.dumps({"error": "'fasting_glucose_mg_dL' is required."}),
            status_code=400,
            mimetype="application/json",

        )   
    try:
        fg_val = float(fg)
    except (TypeError, ValueError):
        return func.HttpResponse(
            json.dumps({"error": "'fasting_glucose_mg_dL' must be a number."}),
            status_code=400,
            mimetype="application/json",

        )
    if fg_val < 100:
        status = "Normal"
        category = "Normal (<100 mg/dL)"   
    elif 100 <= fg_val <= 125:
        status = "Prediabetes"
        category = "Prediabetes (100-125 mg/dL)"
    else:
        status = "Diabetes"
        category = "Diabetes (≥126 mg/dL)"

    payload = {
        "fasting_glucose_mg_dL": fg_val,
        "status": status,
        "category": category,

    }
    return func.HttpResponse(
        json.dumps(payload),
        status_code=200,
        mimetype="application/json",

    ) 







