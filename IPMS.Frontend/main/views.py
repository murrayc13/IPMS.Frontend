from django.shortcuts import render
import requests
import json

def home(request):
    # show_graph()
    return render(request, 'index.html')


def get_minimum_variance(request):
    if request.method == "POST":
        try:
            asset_info = json.loads(request.POST.get("asset_info", "[]"))
            covariance = json.loads(request.POST.get("covariance", "[]"))

            json_payload = {
                "AssetInformation": asset_info,
                "Covariance": covariance
            }

            json_payload_line = {
                "AssetInformation": asset_info,
                "Covariance": covariance,
                "ExpectedReturn": 0.08
            }

            response = requests.post(
                "http://127.0.0.1:5000/minimum-portfolio",
                json=json_payload
            )

            response_line = requests.post(
                "http://127.0.0.1:5000/minimum-variance-line",
                json=json_payload_line
            )

            response.raise_for_status()
            data = response.json()

            response_line.raise_for_status()
            data_line = response_line.json()

        except (ValueError, json.JSONDecodeError) as parse_error:
            data = {"error": f"Invalid input format: {parse_error}"}
            data_line = {"error": f"Invalid input format: {parse_error}"}
        except requests.RequestException as api_error:
            data = {"error": str(api_error)}
            data_line = {"error": str(api_error)}

        return render(request, 'index.html', {'api_data': data, 'graph_point': data, "graph_line": data_line})

    return render(request, 'index.html', {'api_data': "Invalid request", 'graph_point': None})