# programmeerimise-alused
Programmeerimise alused 2021 kevad KJPG

## Giti õpetus
### 1. Repo tegemine
Repo saab teha aadressil: https://github.com/new

Pange nimeks "programmeerimise-alused"

### 2. Ligipääsu lisamine
Kõigepealt andke kõikidele tiimiliikmetele luba repot muuta.

Settings -> Manage access -> Invite a collaborator 

### 3. Giti paigaldamine
Windows: https://gitforwindows.org/

Mac: https://git-scm.com/download/mac

Linux: https://git-scm.com/download/linux

### 3. Repo kloonimine
Kloonige repo enda arvutisse käsuga `git clone <repo aadress>`

Minu repo puhul näiteks:

`git clone https://github.com/ndri/programmeerimise-alused` või `git clone https://github.com/ndri/programmeerimise-alused.git`

Pärast seda peaks tulema kaust programmeerimise-alused sinna, kus te selle käsu jooksutasite.

### 4. Muudatuste salvestamine
Kui teete oma programmis muudatused, peab need üles lükkama.

Saate kasutada `git status`, et näha, kas on vaja faile lisada, commitida või kas olete valmis pushimiseks.

Commititavate failide valimine: `git add failinimi.txt` või `git add *` kõikide failide jaoks.

Commitimine: `git commit -m "Lisasin mängu draakoni"`

Üleslaadimine ehk pushimine: `git push`

Siis küsitakse GitHubi kasutajanime ja parooli. Tundub, et [varsti](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/) läheb see keerulisemaks, aga praegu veel saab.

### 5. Muudatuste allalaadimine
Kui keegi teine on teie repos muudatusi teinud, saate need alla laadida käsuga `git pull`.

See on suht kõik, mis vaja on. Kui keegi on vahepeal repot muutnud ja te proovite neid üles lükata, siis läheb merge'imiseks. Proovige seda praegu vältida.

Lihtne juhis kõigeks vajaminevaks: https://rogerdudler.github.io/git-guide/
