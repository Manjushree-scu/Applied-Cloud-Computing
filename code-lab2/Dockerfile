# as of 9/26/22 latest python
From python:3.10.7
RUN apt-get update
USER root

RUN pip3 install jupyter

ENV JUPYTER_USER our_user
RUN useradd -ms /bin/bash ${JUPYTER_USER}

EXPOSE 8888

USER ${JUPYTER_USER}
RUN pip install pandas numpy seaborn matplotlib sklearn IPython pycountry_convert
WORKDIR /home/${JUPYTER_USER}
RUN pip freeze > requirements.txt

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb 
RUN wget https://raw.githubusercontent.com/Manjushree-scu/Applied-Cloud-Computing/main/python-project/Python-Project-applied.ipynb
RUN wget https://github.com/Manjushree-scu/Applied-Cloud-Computing/blob/main/python-project/Fat_Supply_Quantity_Data.csv
RUN wget https://github.com/Manjushree-scu/Applied-Cloud-Computing/blob/main/python-project/Protein_Supply_Quantity_Data.csv

CMD jupyter notebook --ip=0.0.0.0 --port 8888
