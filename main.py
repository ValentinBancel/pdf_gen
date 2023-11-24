#!/usr/bin/env python
import PyPDF2

def fusionner_pdf(input_path, chemin_sortie, pattern, nombre_de_pdf, nom_fichier_sortie):
    # Créer un objet PDFWriter pour écrire le fichier de sortie
    ecrivain_pdf = PyPDF2.PdfWriter()
    for i in range(1, nombre_de_pdf + 1):
    # Ouvrir les fichiers PDF en mode binaire
        with open(input_path + pattern + str(i) +".pdf", 'rb') as fichier_pdf1:
            # Créer des objets PDFReader pour chaque fichier
            lecteur_pdf1 = PyPDF2.PdfReader(fichier_pdf1)

            # Ajouter toutes les pages du premier PDF
            for num_page in range(len(lecteur_pdf1.pages)):
                page = lecteur_pdf1.pages[num_page]
                ecrivain_pdf.add_page(page)

    # Écrire le fichier de sortie
    with open(chemin_sortie + nom_fichier_sortie, 'wb') as fichier_sortie:
        ecrivain_pdf.write(fichier_sortie)

def is_path_valid(path):
    # Vérifier si le chemin est valide
    if path[:-1] == '/':
        return path
    else:
        path += '/'
    return path

if __name__ == '__main__':
    pdf_input = input("Entrez le chemin des pdf à fusionner: ")
    pdf_output = input("Entrez le chemin de sortie: ")
    pdf_file_output = input("Entrez le nom du fichier de sortie: ")
    pdf_number = int(input("Entrez le nombre de pdf à fusionner: "))
    pdf_pattern = input("Entrez le pattern des pdf à fusionner: ")

    pdf_input = is_path_valid(pdf_input)
    pdf_output = is_path_valid(pdf_output)

    fusionner_pdf(pdf_input, pdf_output, pdf_pattern, pdf_number, pdf_file_output)