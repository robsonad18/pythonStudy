import xmltodict
import os
import pandas as pd

def get_infos(name_file, values):
    with open(f'files/nfs/{name_file}', "rb") as file_xml:
        dic_file = xmltodict.parse(file_xml)

        if "NFe" in dic_file:
            infos_nf = dic_file["NFe"]['infNFe']
        else:
            infos_nf = dic_file['nfeProc']["NFe"]['infNFe']
            
        number_nf = infos_nf["@Id"]
        company_broadcaster = infos_nf['emit']['xNome']
        name_client = infos_nf["dest"]["xNome"]
        address = infos_nf["dest"]["enderDest"]
        
        weight = "Não informado"
        if "vol" in infos_nf["transp"]:
            weight = infos_nf["transp"]["vol"]["pesoB"]
        
        values.append([number_nf, company_broadcaster, name_client, address, weight])

try:
    path_files = input("Digite o caminho da pasta que consta as notas fiscais: ")
    list_files = os.listdir(path_files)

    colunas = ["Numero da nota", "Companha emissora", "Nome do cliente", "Endereço", "Peso"]
    values = []
    for file_current in list_files:
        get_infos(file_current, values)

    table_return = pd.DataFrame(columns=colunas, data=values)
    table_return.to_excel("notasfiscais.xlsx", index=False)

    print("Arquivo excel das notas fiscais foi gerado com sucesso!")
except:
    print("Erro ao gerar arquivo excel das notas fiscais")