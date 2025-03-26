import asyncio
import json
from ollama import AsyncClient

async def chat():
    """
    Stream a chat from Llama using the AsyncClient.
    """
    data ={
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
        "content": "Jesteś ekspertem w wykrywaniu elektronicznych chronionych informacji w elektronicznych dokumentach zdrowotnych."
                   "Proszę zidentyfikować w poniższym słowniku JSON wszystkie podmioty z wraźliwą informacją, zawierającą imiona i nazwiska:"
                   ""
                   + formatted_string +
                   ''
                   "Proszę zwrócić TYLKO wartości zidentyfikowanych podmiotów w formacie JSON."
    }
    async for part in await AsyncClient().chat(
        model="llama3.1", messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


asyncio.run(chat())