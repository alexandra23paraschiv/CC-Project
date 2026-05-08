Proiect Cloud Computing
Cat Facts Studio

Paraschiv Alexandra Maria
1153 SIMPRE

Link-uri
Aplicație: https://random-cat-fact.onrender.com
Github: https://github.com/alexandra23paraschiv/CC-Project
Link video: https://youtu.be/BU3ooMeYIeQ


Introducere
Aplicațiile web sunt instrumente esențiale în era digitală, oferind acces rapid și facil la diverse informații și servicii. Cat Facts Studio App oferă utilizatorilor o experiență simplă și plăcută pentru a descoperi curiozități interesante despre pisici, cu traduceri automate în limba română.
Această aplicație reduce plictiseala și face informațiile despre pisici disponibile într-un mod rapid și accesibil, printr-un singur click.


Descriere problemă
Deși limba engleză este utilizată pe scară largă pe internet, mulți utilizatori nu o stăpânesc fluent. Aceasta limitează accesul la informație și afectează experiența online. În plus, nu toți utilizatorii au acces constant la servicii avansate de traducere.
Pentru a depăși aceste bariere, Cat Facts Studio App integrează traducerea automată prin API-ul MyMemory, astfel încât textele afișate să fie disponibile imediat și clar în limba română. Aceasta crește accesibilitatea și îmbunătățește experiența utilizatorului.


Descriere API
Aplicația folosește trei servicii externe prin API REST:
•	Cat Fact API
Sursa principală de date este https://catfact.ninja/fact, un API public care oferă fapte random despre pisici în limba engleză.
•	MyMemory Translation API
Pentru traducerea automată a textului, aplicația folosește API-ul MyMemory. Printr-o cerere GET către https://api.mymemory.translated.net/get, textul în engleză este tradus în limba română folosind parametrul `langpair=en|ro`.
Acest mecanism oferă o traducere gratuită și simplă, fără a necesita un API key.
•	Mongo DB
Pentru a salva în baza de date faptele generate.


Tehnologii folosite
Aplicația este construită folosind următoarele tehnologii:
•	Backend:
Flask (Python) — pentru expunerea serviciilor web și integrarea cu API-urile externe.
•	Frontend:
HTML și CSS simplu, pentru o interfață ușor de utilizat și adaptabilă.
•	Requests (Python):
Biblioteca utilizată pentru efectuarea cererilor HTTP către API-urile externe.
•	MyMemory API:
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
b.	Request de tip POST pentru a obține traducerea în limba română

2.	Metode HTTP folosite
a.	GET pentru a obține un random cat fact
b.	POST pentru a traduce în română acel fact

3.	Autentificare și servicii utilizate
Utilizarea API-ului https://catfact.ninja/fact este gratuită și nu necesită API key.
Utilizarea API-ului MyMemory pentru traducere este gratuită și nu necesită autentificare.


Referințe

1.	https://mymemory.translated.net/
2.	https://catfact.ninja/
3.	https://flask.palletsprojects.com/
4.	https://requests.readthedocs.io/en/latest/
5.	https://render.com/
6.	https://github.com/
