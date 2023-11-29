from pypdf import PdfMerger
import sys

# merger = PdfMerger()

# for pdf in sys.argv[:-1]:
#     merger.append(str(pdf)

# merger.write(sys.argv[-1])
# merger.close()


merger = PdfMerger()

pdfs = ["s-nhohnn_pk_03_q1_3_6.pdf", "s-nhohnn_pk_03_q2.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()