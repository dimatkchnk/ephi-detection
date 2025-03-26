import asyncio
import json
from ollama import AsyncClient

async def chat():
    """
    Stream a chat from Llama using the AsyncClient.
    """
    data = {
        "SOPClassUID": "1.2.840.10008.5.1.4.1.1.2",
        "SOPInstanceUID": "1.3.6.1.4.1.16677.1.1735574618255014000",
        "StudyDate": "19710221",
        "SeriesDate": "19580809",
        "ContentDate": "19730706",
        "AcquisitionDateTime": "20111119",
        "Modality": "CT",
        "Manufacturer": "ModernCTQ",
        "ReferringPhysicianName": "XJARMOCHIN",
        "PhysiciansOfRecord": "TRONINO",
        "PerformingPhysicianName": "XSZABOR",
        "NameOfPhysiciansReadingStudy": "XSYWYKO",
        "OperatorsName": "ZYKOX",
        "StudyDescription": "LEGS ACA",
        "SeriesDescription": "LEGS AX",
        "ManufacturerModelName": "Super256",
        "PatientName": "SYWYKOX",
        "PatientID": "34",
        "OtherPatientIDsSequence": "15",
        "OtherPatientIDs": "39",
        "PatientBirthDate": "19940402",
        "PatientSex": "F",
        "PatientAge": "050Y",
        "PatientWeight": "68.0",
        "AcquisitionDate": "20130825"
    }

    json_string = json.dumps(data, indent=4)
    formatted_string = "'{\n" + json_string[1:-1].replace('    ', '').replace('\n', '').replace(',', ',\n') + "\n}'"
    message = {
        "role": "user",
        "content": "You are an expert in detecting electronic protected health information in electronic health documents."
                   "List of all possible surnames or last names in electronic health documents:"
                   "[NOWAK, KOWALSKI, WISNIEWSKI, WOJCIK, KOWALCZYK, KAMINSKI, LEWANDOWSKI, ZIELINSKI, WOZNIAK, SZYMANSKI, DABROWSKI, KOZLOWSKI, MAZUR, JANKOWSKI, KWIATKOWSKI, WOJCIECHOWSKI, KRAWCZYK, KACZMAREK, PIOTROWSKI, GRABOWSKI, ZAJAC, PAWLOWSKI, KROL, MICHALSKI, WROBEL, WIECZOREK, JABLONSKI, NOWAKOWSKI, MAJEWSKI, OLSZEWSKI, DUDEK, JAWORSKI, STEPIEN, MALINOWSKI, ADAMCZYK, GORSKI, PAWLAK, SIKORA, NOWICKI, WITKOWSKI, RUTKOWSKI, WALCZAK, BARAN, MICHALAK, OSTROWSKI,"
                   "SZEWCZYK, TOMASZEWSKI, ZALEWSKI, WROBLEWSKI, PIETRZAK, JASINSKI, DUDA, MARCINIAK, SADOWSKI, BAK, ZAWADZKI, JAKUBOWSKI, WILK, CHMIELEWSKI, BORKOWSKI, WLODARCZYK, SOKOLOWSKI, SZCZEPANSKI, SAWICKI, LIS, KUCHARSKI, KALINOWSKI, WYSOCKI, MAZUREK, KUBIAK, MACIEJEWSKI, KOLODZIEJ, KAZMIERCZAK, CZARNECKI, KONIECZNY, SOBCZAK, KRUPA, GLOWACKI, URBANSKI, MROZ, KOZAK, ZAKRZEWSKI, WASILEWSKI, KRAJEWSKI, LASKOWSKI, SIKORSKI, ZIOLKOWSKI, GAJEWSKI, SZULC, MAKOWSKI,"
                   "KACZMARCZYK, BRZEZINSKI, BARANOWSKI, PRZYBYLSKI, KANIA, SZYMCZAK, JANIK, BOROWSKI, ADAMSKI, BLASZCZYK, GORECKI, SZCZEPANIAK, CHOJNACKI, KOZIOL, MUCHA, LESZCZYNSKI, LIPINSKI, ANDRZEJEWSKI, KOWALEWSKI, CZERWINSKI, WESOLOWSKI, MIKOLAJCZYK, ZIEBA, JAROSZ, CIESLAK, KOWALIK, MARKOWSKI, MUSIAL, KOLODZIEJCZYK, KOPEC, BRZOZOWSKI, NOWACKI, PIATEK, ZAK, DOMANSKI, PAWLIK, ORLOWSKI, KUREK, KOT, WOJTOWICZ, CIESIELSKI, TOMCZYK, TOMCZAK, KRUK, WAWRZYNIAK, POLAK, WOLSKI]"
                   "Please identify in the following JSON dictionary all entities with names and surnames which are included in the list above:"
                   ""
                   + formatted_string +
                   ''
                   "Please return ONLY the values of identified entities in JSON format."
    }
    async for part in await AsyncClient().chat(
        model="llama3.1", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


asyncio.run(chat())