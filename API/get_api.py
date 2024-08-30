import requests
import json
import os

with open("config.json", "r") as f:
    token = json.load(f)["token"]


class Clima:
    @staticmethod
    def buscar_cidades(estado):
        payload = {"token": token, "state": estado}

        try:
            r = requests.get(
                "http://apiadvisor.climatempo.com.br/api/v1/locale/city", params=payload
            )
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"Erro ao fazer a solicitação: {e}")
            return None

    def buscar_clima(cidade):
        payload = {"token": token}

        try:
            r = requests.get(
                f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{cidade}/current",
                params=payload,
            )
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"Erro ao fazer a solicitação: {e}")
            return None

    def buscar_clima_15_dias(cidade):
        payload = {"token": token}

        try:
            r = requests.get(
                f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{cidade}/days/15",
                params=payload,
            )
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"Erro ao fazer a solicitação: {e}")
            return None
