# Bot Cisco Webex Teams - Gitlab


### Flask
Flask permet aux hooks des services webex et gitlab de pouvoir taper sur l'app.

### Ngrok
Ngrok nous permet d'host l'application en local et d'ouvrir un accès au monde du dehors à notre machine.  

**Ce bot n'est pas fonctionnel tel quel.**  
Vous avez besoin des droits admin sur gitlab pour avoir l'autorisation de créer des webhooks chez ce dernier.  
Puis je l'ai développé à des fins personnels, beaucoup de choses sont propres a des projets perso:
- Label
- ID du projet gitlab
- URLs

Je vous invite à bien faire le tour si vous souhaitez l'utiliser.

### Comment ça marche ?

Vous aurez besoin de clé d'authorisations de chaque côté:
- [Cisco Webex Developers](https://developer.webex.com/)
- Gitlab > Settings > Access Tokens

1.
```bash
git clone https://github.com/Peskoo/cisco-teams-bot.git
```
```bash
pip install flask
pip install webexteamssdk
```
Installer ngrok en allant par [ici](https://ngrok.com/).

Crée un fichier `secrets.json` à la racine du projet et remplacez par vos clés.
```json
{
    "gitlab": "your_access_key",
    "webex": "your_access_key"
}
```
2.
```bash
ngrok http 8080
```
```bash
python main.py
```
Puis dans webex, ouvrez une conversation avec `gitoune@webex.bot`.

#### Commandes
```bash
/mr     # Récupérer les merges requests qui vous sont assignées, avec le label 'For Review'
/all    # Vous dit combien de merges requests en attente de review vous sont assignées.
```
