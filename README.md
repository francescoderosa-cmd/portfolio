# Portfolio — Francesco de Rosa

Sito portfolio personale (Digital & Service Design Lead). Singolo file `index.html`,
nessuna build, nessuna dipendenza: si apre col doppio clic e si pubblica così com'è.

## Struttura

| File         | A cosa serve                                                            |
|--------------|-------------------------------------------------------------------------|
| `index.html` | Tutto il sito: home + 5 case study (Grenada, HungerMap, CBT, CashBook, Legacy). La navigazione tra le "pagine" è gestita in JavaScript (single-page). |
| `CNAME`      | Dominio personalizzato per GitHub Pages. **Da modificare** col tuo dominio. |
| `.gitignore` | Esclude l'installer di Git e i file di sistema dal repository.          |

## Anteprima locale

Doppio clic su `index.html`, oppure da terminale per un server locale:

```powershell
python -m http.server 8000
# poi apri http://localhost:8000
```

## Pubblicazione su GitHub Pages

1. Crea un repository su GitHub (es. `portfolio` o `francescoderosa.github.io`).
2. Collega questa cartella e pusha:
   ```powershell
   git remote add origin https://github.com/<tuo-utente>/<repo>.git
   git branch -M main
   git push -u origin main
   ```
3. Su GitHub → **Settings → Pages** → *Build and deployment* → Source: **Deploy from a branch**, branch `main`, cartella `/ (root)`. Salva.
4. Dopo ~1 minuto il sito è online su `https://<tuo-utente>.github.io/<repo>/`.

## Dominio personalizzato

Hai detto di volere un dominio tuo (es. `francescoderosa.com`):

1. **Compra il dominio** da un registrar (Namecheap, Cloudflare, GoDaddy… ~10€/anno).
2. **Modifica il file `CNAME`** in questa cartella mettendo il tuo dominio reale
   (una sola riga, senza `https://`). Ora contiene un segnaposto: `francescoderosa.com`.
3. Nel pannello DNS del registrar aggiungi:
   - 4 record **A** verso gli IP di GitHub Pages:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - (per il sottodominio `www`) un record **CNAME** `www` → `<tuo-utente>.github.io`
4. Su GitHub → **Settings → Pages → Custom domain**: inserisci il dominio, salva,
   poi spunta **Enforce HTTPS** (compare dopo che il certificato è pronto).

> Se NON vuoi un dominio custom, elimina semplicemente il file `CNAME`: il sito
> resterà raggiungibile sull'indirizzo `*.github.io` gratuito.

## Cose da aggiornare prima di andare live

- **Link LinkedIn**: in `index.html` è impostato su
  `https://www.linkedin.com/in/francescoderosa` — sostituiscilo con l'URL reale del tuo profilo.
- **Foto / immagini**: il sito usa solo grafica vettoriale e colori, nessuna foto.
  Se vuoi aggiungere immagini reali dei progetti, mettile in una cartella `assets/`.
