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
            covariance = json.loads(request.POST.get("correlation", "[]"))
            expected_return = json.loads(request.POST.get("expected_return", "[]"))

            json_payload = {
                "AssetInformation": asset_info,
                "Correlation": covariance,
                "ExpectedReturn": expected_return
            }

            response = requests.post(
                "http://127.0.0.1:5000/minimum-portfolio",
                json=json_payload
            )

            response.raise_for_status()
            data = response.json()

        except (ValueError, json.JSONDecodeError) as parse_error:
            data = {"error": f"Invalid input format: {parse_error}"}
        except requests.RequestException as api_error:
            data = {"error": str(api_error)}

        return render(request, 'index.html', {
            'api_data': data["Minimum Portfolio"], 'graph_point': data["Minimum Portfolio"], "graph_line": data['Minimum Frontier']
        })

    return render(request, 'index.html', {'api_data': "Invalid request", 'graph_point': None})