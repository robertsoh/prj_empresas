from io import BytesIO
from datetime import datetime

import pytesseract
import requests
from PIL import Image
from bs4 import BeautifulSoup

from apps.empresa.models import TipoContribuyente

captcha_url = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image'
url = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias'


def procesar_imagen_captcha(session):
    response = session.get(captcha_url)
    if response.status_code == 200:
        im = Image.open(BytesIO(response.content))
        return pytesseract.image_to_string(im)
    return None


def preparar_data(ruc, captcha):
    return {
        'accion': 'consPorRuc',
        'razSoc': '',
        'nroRuc': ruc,
        'nrodoc': '',
        'contexto': 'ti-it',
        'tQuery': 'on',
        'search1': ruc,
        'codigo': captcha,
        'tipdoc': '1',
        'search2': '',
        'coddpto': '',
        'codprov': '',
        'coddist': '',
        'search3': '',
    }


def procesar_resultado(raw_html):
    soup = BeautifulSoup(raw_html, 'lxml')
    try:
        trs = soup.find_all('table')[0].find_all('tr')
        ruc, nombre = trs[0].find_all('td')[1].text.strip().split(' - ')
        str_tipo_contribuyente = trs[1].find_all('td')[1].text.strip()
        nombre_comercial = trs[3].find_all('td')[1].text.strip()
        str_fecha_inscripcion = trs[4].find_all('td')[1].text.strip()
        estado = trs[5].find_all('td')[1].text.strip()
        condicion = trs[6].find_all('td')[1].text.strip()
        domicilio_fiscal = trs[7].find_all('td')[1].text.strip()
        try:
            fecha_inscripcion = datetime.strptime(str_fecha_inscripcion, '%d/%m/%Y')
        except Exception:
            fecha_inscripcion = None
        try:
            tipo_contribuyente = TipoContribuyente.objects.get(codigo=str_tipo_contribuyente)
        except TipoContribuyente.DoesNotExist:
            tipo_contribuyente = None
        data = {
            'ruc': ruc,
            'nombre': nombre,
            'fecha_inscripcion': fecha_inscripcion,
            'tipo_contribuyente': tipo_contribuyente,
            'nombre_comercial': nombre_comercial,
            'estado': estado,
            'condicion': condicion,
            'domicilio_fiscal': domicilio_fiscal
        }
        print(data)
        return data
    except (IndexError, ValueError):
        return {}


def buscar_ruc(ruc):
    """
    Retorna un diccionario con la data de la empresa
    """
    with requests.Session() as s:
        code = procesar_imagen_captcha(s)
        if code:
            data = preparar_data(ruc, code)
            response = s.post(url, data=data)
            return procesar_resultado(response.content)
    return {}
