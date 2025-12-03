from pathlib import Path
from docx import Document
from PyPDF2 import PdfReader
import shutil


documents = Path(r"") # Dossier contenant les documents en vrac

dossier_annonce = Path(r"") # Dossier où seront déplacés les annonces

dossier_CV = Path(r"") # Dossier où seront déplacés les CV

data=[]
for pattern in ("*.docx", "*.pdf"):
    for file in documents.glob(pattern):
        data.append(file)

keywords_cv = [
        "experience", "competence", "formation", "profil", "curriculum",
        "contact", "diplome", "langues", "logiciels"
    ]

keywords_annonce = [
        "mission", "entreprise", "poste", "responsabilites",
        "profil recherche", "profil recherché", "salaire", "candidature",
        "contrat", "recrutement"
    ]

for i in range(len(data)):
    
    if data[i].suffix.lower() == ".docx":
        texte="\n".join(p.text for p in Document(data[i]).paragraphs)
    
    if data[i].suffix.lower() == ".pdf":
        with open(data[i], "rb") as f:
            reader = PdfReader(f)
            texte = "\n".join(page.extract_text() or "" for page in reader.pages)
    
    score_cv=sum(texte.count(mot) for mot in keywords_cv)
    score_annonce=sum(texte.count(mot) for mot in keywords_annonce)

    if score_cv > 1 or score_annonce > 1:

        if score_cv < score_annonce:
            shutil.move(str(data[i]), str(dossier_annonce))
        
        elif score_cv >= score_annonce:
            shutil.move(str(data[i]), str(dossier_CV))
    
    else:
        continue