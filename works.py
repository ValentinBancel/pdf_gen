def fusionner_pdf(chemin_pdf1, chemin_pdf2, chemin_sortie):
    # Ouvrir les fichiers PDF en mode binaire
    with open(chemin_pdf1, 'rb') as fichier_pdf1, open(chemin_pdf2, 'rb') as fichier_pdf2:
        # Créer des objets PDFReader pour chaque fichier
        lecteur_pdf1 = PyPDF2.PdfReader(fichier_pdf1)
        lecteur_pdf2 = PyPDF2.PdfReader(fichier_pdf2)

        # Créer un objet PDFWriter pour écrire le fichier de sortie
        ecrivain_pdf = PyPDF2.PdfWriter()

        # Ajouter toutes les pages du premier PDF
        for num_page in range(len(lecteur_pdf1.pages)):
            page = lecteur_pdf1.pages[num_page]
            ecrivain_pdf.add_page(page)

        # Ajouter toutes les pages du deuxième PDF
        for num_page in range(len(lecteur_pdf2.pages)):
            page = lecteur_pdf2.pages[num_page]
            ecrivain_pdf.add_page(page)

        # Écrire le fichier de sortie
        with open(chemin_sortie, 'wb') as fichier_sortie:
            ecrivain_pdf.write(fichier_sortie)