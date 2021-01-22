from flask import Flask
from flask import Flask, request, jsonify, g, render_template, redirect, Response
import csv
import requests


app = Flask(__name__)

#aqui nao precisa usar beautiful ou scrapy
@app.route('/<d1>/<d2>', methods=['GET'])
def example(d1,d2):

	CSV_URL = 'https://www.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&amp;ChkMoeda=61&amp;DATAINI='+d1+'&amp;DATAFIM='+d2

	with requests.Session() as s:
	    download = s.get(CSV_URL)

	    decoded_content = download.content.decode('utf-8')

	    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
	    my_list = list(cr)
	    for row in my_list:
	        print(row)


	resp = {
		"status":200,
		"value":my_list,
	}
	
	return jsonify(resp)

if __name__ == "__main__":
	app.run(host='0.0.0.0')

