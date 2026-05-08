Proiect Cloud Computing
Random cat fact

Paraschiv Alexandra Maria
1153 SIMPRE

Link-uri
Aplicație: https://random-cat-fact.onrender.com
Github: https://github.com/alexandra23paraschiv/CC-Project
Link video: https://youtu.be/BU3ooMeYIeQ


Introducere
Aplicațiile web sunt instrumente esențiale în era digitală, oferind acces rapid și facil la diverse informații și servicii. În acest context, Random Cat Fact App vine să ofere utilizatorilor o experiență simplă și plăcută pentru a descoperi curiozități interesante despre pisici, traduse automat în limba română pentru o accesibilitate mai mare.
Această aplicație combate active plictiseala. Astfel, utilizatorii pot obține rapid și ușor informații utile și distractive, în limba română, printr-un singur click.


Descriere problemă
Chiar dacă limba engleză este utilizată pe scară largă pe internet, un procent semnificativ din populație nu o stăpânește fluent. Aceasta limitează accesul la informație și poate reduce experiența utilizatorului. Mai mult, nu toți utilizatorii au acces constant la internet, ceea ce îngreunează folosirea serviciilor de traducere online în timp real.
Pentru a depăși aceste bariere, Random Cat Fact App integrează un serviciu de traducere automatizată prin API-ul DeepL, astfel încât textele afișate să fie disponibile imediat și clar în limba română. Aceasta crește accesibilitatea și îmbunătățește experiența utilizatorului, făcând aplicația utilă unui public mai larg.


Descriere API
Aplicația folosește două servicii cloud prin API REST:
•	Cat Fact API
Sursa principală de date este https://catfact.ninja/fact, un API public care oferă fapte random despre pisici în limba engleză.
•	DeepL API
Pentru traducerea automată a textului, aplicația folosește API-ul DeepL, unul dintre cele mai avansate servicii de traducere automată disponibile. Printr-o cerere POST către https://api-free.deepl.com/v2/translate, textul în engleză este tradus în limba română (sau orice altă limbă selectată).
Acest mecanism oferă traduceri rapide, precise și permite adaptarea conținutului în funcție de nevoile utilizatorului.
•	Mongo DB
Pentru a salva într-o bază de date fact-urile generate.


Tehnologii folosite
Aplicația este construită folosind următoarele tehnologii:
•	Backend:
Flask (Python) — pentru expunerea serviciilor web și integrarea cu API-urile externe.
•	Frontend:
HTML și CSS simplu, pentru o interfață ușor de utilizat și adaptabilă.
•	Requests (Python):
Biblioteca utilizată pentru efectuarea cererilor HTTP către API-urile externe.
•	DeepL API:
Serviciul cloud pentru traduceri automate.
•	Cat Fact API:
Sursa datelor despre pisici.
•	GitHub:
Pentru versionarea codului și colaborare.
•	Render.com:
Pentru hostarea aplicației și acces public.


Flux de date

1.	Exemple de requesturi
a.	Request de tip GET pentru a obține un random cat fact
b.	Request de tip POST pentru a obtine o traducere

2.	Metode HTTP folosite
a.	GET pentru a obține un random cat fact
b.	POST pentru a traduce in română acel fact

3.	Authentificare și servicii utilizate
Utilizarea API ului https://catfact.ninja/fact este gratis și nu necesită un API KEY.
Utilizarea API ului de traducere este de asemenea gratis pana la 500.000 de caractere, dar necesită un API KEY pe care îl poti obține la crearea unui cont.


Referințe

1.	https://developers.deepl.com/docs/
2.	https://catfact.ninja/
3.	https://flask.palletsprojects.com/
4.	https://requests.readthedocs.io/en/latest/
5.	https://render.com/
6.	https://github.com/
