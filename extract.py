import PyPDF2

def extract_pdf(file_extract, pattern):
    # Créer un objet PDFWriter pour écrire le fichier de sortie
    ecrivain_pdf = PyPDF2.PdfWriter()
    # Ouvrir les fichiers PDF en mode binaire
    with open(file_extract, 'rb') as fichier_pdf1:
        # Créer des objets PDFReader pour chaque fichier
        lecteur_pdf1 = PyPDF2.PdfReader(fichier_pdf1)

        # Ajouter toutes les pages du premier PDF
        for num_page in range(len(lecteur_pdf1.pages)):
            page = lecteur_pdf1.pages[num_page]
            ecrivain_pdf.add_page(page)
                    # Écrire le fichier de sortie
            with open("./extract/"+pattern + str(num_page + 1) + ".pdf", 'wb') as fichier_sortie:
                ecrivain_pdf.write(fichier_sortie)

if __name__ == '__main__':
    file_to_extract = input("Entrez le nom du fichier à extraire: ")
    pattern = input("Entrez le pattern des pdf de sortie: ")
    extract_pdf(file_extract=file_to_extract, pattern=pattern)