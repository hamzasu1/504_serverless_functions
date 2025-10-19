import json
import functions_framework

@functions_framework.http
def glucose_http(request):
    """HTTP Cloud Function.
    Expects JSON with 'fasting_glucose_mg_dL'
    Returns a JSON classification of fasting glucose. Utilizing ada sample ranges
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    fg = data.get("fasting_glucose_mg_dL", args.get("fasting_glucose_mg_dL"))


    # Presence check
    if fg is None:
        return (
            json.dumps({"error": "'fasting_glucose_mg_dL' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        fg_val = float(fg)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'fasting_glucose_mg_dL' must be a number."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Ranges off of citations
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

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
