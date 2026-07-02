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
2. **Crea un file `CNAME`** in questa cartella con dentro il tuo dominio reale
   (una sola riga, senza `https://`, es. `francescoderosa.com`), poi commit e push.
3. Nel pannello DNS del registrar aggiungi:
   - 4 record **A** verso gli IP di GitHub Pages:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - (per il sottodominio `www`) un record **CNAME** `www` → `<tuo-utente>.github.io`
4. Su GitHub → **Settings → Pages → Custom domain**: inserisci il dominio, salva,
   poi spunta **Enforce HTTPS** (compare dopo che il certificato è pronto).

> Finché non aggiungi il file `CNAME`, il sito resta raggiungibile sull'indirizzo
> `*.github.io` gratuito.

## The Lab: aggiungere un'opera

La galleria di `lab.html` è guidata da `assets/lab/works.js`. Per aggiungere un progetto:

1. Metti le immagini ottimizzate (`.webp`, max ~1400px) in `assets/lab/`.
2. Aggiungi una entry all'array `WORKS` in `assets/lab/works.js`
   (lo schema è documentato in testa al file: id, type, title, cover, images,
   meta opzionale, `ba` opzionale per lo slider prima/dopo).
3. Copia un blocco `<article class="card">` in `lab.html` e aggiorna
   `data-id`, `data-type`, immagine e didascalia.

I filtri, la vista dettaglio, lo slider prima/dopo e i deep link (`#/w/<id>`)
funzionano da soli in base ai dati.
