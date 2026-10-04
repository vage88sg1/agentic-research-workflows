# Galileo — Guida rapida

**Descrivi cosa vuoi ottenere. Galileo sceglie il percorso e ti accompagna nel lavoro.**

Galileo contiene istruzioni `SKILL.md` e strumenti locali utilizzabili con diversi assistenti AI (harness). Il client fornisce modelli, agenti e ambiente di esecuzione. Dopo l'installazione chiedi di usare la skill **Galileo** e descrivi il tuo obiettivo. Non serve imparare i nomi dei workflow o compilare file di configurazione.

| Harness | Cartella delle skill nel progetto | Avvio |
|---|---|---|
| Claude Code | `.claude/skills/` | `/galileo` seguito dalla richiesta |
| Codex | `.agents/skills/` | `$galileo` oppure Galileo nel menu delle skill disponibile |
| OpenCode | `.opencode/skills/` | Chiedi di caricare la skill Galileo |
| GitHub Copilot, in una modalità con supporto alle skill | `.github/skills/` | Chiedi di usare la skill Galileo |
| Altri harness compatibili | Cartella indicata dalla loro documentazione | Menu o sintassi previsti dal client |

I percorsi sono documentati dai client; non implicano un collaudo completo su ciascuno. L'installer non registra un comando `/` universale. Fonti e limiti sono nella [guida di installazione](INSTALLATION.md).

## Tutte le funzionalità

Il profilo completo contiene **Galileo, nove workflow specialistici e undici skill di supporto: 21 cartelle di skill**.

| Funzionalità | Cosa offre |
|---|---|
| Guida e ripresa del lavoro | Domande progressive, riuso delle risposte, stato salvato e passaggi tra i workflow richiesti |
| Agenti e correzioni | Ruoli specialistici, delegazione quando disponibile e autorizzata, revisori distinti e loop con limiti espliciti |
| Completezza e revisione della versione finale | Distingue materiali mancanti da fonti presenti ma escluse; verifica adeguatezza allo scopo, terminologia e leggibilità. I controlli indicano la versione esaminata e le revisioni ancora pendenti |
| Stesura scientifica | Sviluppo per sezioni, checkpoint interattivi o avanzamento autonomo, ricerca attiva delle lacune bibliografiche, outline e testo collegati alle evidenze, controlli di disegno/scoring/questionari, analisi e figure quando realmente eseguite |
| Simulazione editoriale | Controllo tecnico, tre peer reviewer anonimi simulati, decisione motivata, risposta agli autori, correzioni e nuova revisione |
| Ricerca bibliografica | PubMed / Europe PMC, OpenAlex, Crossref e Zotero sperimentale; proposte MCP pertinenti e ricerca di altri candidati |
| Formati | DOCX o LaTeX, bibliografia e riferimenti incrociati, PDF con strumenti disponibili nel client |
| Slide e stile | PPTX/PDF o Beamer, storyboard, note, tempi stimati, stili proposti, slide campione e revisione dei render |
| Identità istituzionale | Loghi, colori, font e template del gruppo/università, più affiliazioni e controlli di leggibilità |
| Tesi → articolo e discussione | Mappa delle trasformazioni/omissioni, budget di parole, domande interattive, feedback e slide di riserva |
| Revisione sistematica | Protocollo, ricerca, deduplicazione, screening, estrazione, valutazione e sintesi appropriata |
| Dossier per la rivista | Cover letter, file identificati/anonimizzati quando richiesti, dichiarazioni e checklist; preparazione locale |
| Tracciabilità e riproducibilità | Cinque comandi offline: `preflight`, `evidence`, `impact`, `delivery` e `bundle`; dipendenze registrate, hash, coerenza dei controlli di consegna e file selezionati |
| Qualità e costo | Profili di costo configurabili, contesti mirati, riuso delle evidenze e modelli disponibili nel proprio client |

Sono istruzioni di workflow e strumenti locali: agenti indipendenti, ricerche, calcoli, esportazioni e controlli visivi dipendono dalle capacità reali del client. I risultati non eseguiti non vengono dichiarati completati.

## Scegli il percorso

Non serve imparare i nomi: descrivi l'obiettivo a Galileo. Puoi anche richiamare direttamente questi workflow:

| Workflow | Obiettivo |
|---|---|
| Galileo - Research drafting | Scrivere o migliorare tesi e articoli |
| Galileo - Research review | Simulare peer review, decisione e correzioni |
| Galileo - Research typesetting | Produrre Word, LaTeX e PDF |
| Galileo - Research presentations | Preparare e revisionare slide scientifiche |
| Galileo - Research project | Controllare evidenze, cambiamenti e riproducibilità |
| Galileo - Thesis to article | Convertire una tesi in un articolo mirato |
| Galileo - Research defense | Allenarsi alla discussione e alle domande |
| Galileo - Submission dossier | Preparare i materiali richiesti dalla rivista |
| Galileo - Systematic review | Svolgere una revisione sistematica esplicitamente richiesta |

Il prefisso `Galileo -` compare nei nomi del menu quando il client legge i metadati `agents/openai.yaml`. Gli identificatori e i comandi restano invariati: per esempio, in Codex puoi usare `$research-review`. Il punto di ingresso principale resta **Galileo**.

[Guida completa con esempi e un diagramma per ogni workflow](WORKFLOW_GUIDE.md).

## Scegli i modelli durante l’installazione

Se esegui l’installer in un terminale, Galileo propone una configurazione guidata: harness, modelli disponibili, associazione ai tre alias `economical`, `balanced` e `frontier`, profilo di costo e override facoltativi per singolo ruolo. Puoi usare lo stesso modello per tutti gli alias o rimandare. Il riepilogo viene salvato solo dopo la tua conferma.

Le preferenze sono locali, nel file `galileo-models.json` accanto alle cartelle delle skill. Il workflow verifica le capacità reali del client; se un modello richiesto non è disponibile, chiede come procedere. La configurazione non attiva API a pagamento né cambia le impostazioni del client.

Per script e automazioni usa `--non-interactive`, eventualmente con `--model-settings FILE`. Per riconfigurare una versione già installata usa `--configure-models --replace-model-settings`: conserva un backup e non reinstalla le skill. [Guida completa alla configurazione dei modelli](MODEL_SETUP.md).

## Parti da una richiesta semplice

```text
Usa la skill Galileo e aiutami a scrivere la mia tesi. Ho la descrizione dello studio e i risultati
nella cartella materiali/. Scrivi in italiano e guidami nel prossimo passo.
```

Altri esempi:

- «Migliora questo manoscritto mantenendo i risultati.»
- «Fai una simulazione di peer review e aiutami a rispondere ai commenti.»
- «Trasforma questa tesi in un articolo e poi prepara le slide.»
- «Crea una presentazione di 12 minuti da questo articolo.»
- «Aiutami a preparare la discussione: fammi una domanda alla volta.»
- «Prepara i documenti richiesti da questa rivista.»
- «Aiutami a pianificare una revisione sistematica.»

Galileo usa le informazioni già disponibili, fa le domande necessarie e attiva le competenze pertinenti. Quando serve produrre il documento, chiarisce Word o LaTeX. Per Word, Excel e PowerPoint attiva le skill Office pertinenti: usa strutture native e modificabili quando supportate, verifica campi/formule e dichiara le funzioni non disponibili. Il pacchetto include una skill MIT per DOCX/XLSX/PPTX/PDF e riusa le skill del client, se adatte. [Guida Office](OFFICE_SUPPORT.md). Per LaTeX usa bibliografia, indici, contatori e rimandi automatici, conserva template e motore compatibili e verifica log e PDF finali; il supporto include scrittura accademica e compilazione locale isolata quando adatta. [Guida LaTeX](LATEX_SUPPORT.md). Mantiene nei registri del progetto evidenze, controlli e problemi aperti. Non devi rilanciare un comando per ogni passaggio di un lavoro già richiesto.

Per tesi e articoli completi, Galileo propone un indice e una stesura per sezioni: introduzione provvisoria, poi i capitoli adatti al lavoro. Puoi scegliere checkpoint dopo ogni capitolo o avanzamento autonomo con controlli intermedi; abstract e conclusioni vengono finalizzati dopo metodi/implementazione e risultati/valutazione. La revisione complessiva resta obbligatoria prima della consegna finale.

Per un progetto completo, Galileo verifica prima quali informazioni essenziali sono disponibili e fa domande mirate sui punti mancanti. Il controllo delle evidenze è distinto dalla revisione del linguaggio tecnico e della leggibilità: i termini disciplinari d’uso, anche inglesi in un testo italiano, e i nomi di API/componenti restano coerenti. Per lacune sul progetto fa domande e attende le risposte; per lacune di conoscenza esterna cerca e consulta fonti primarie pertinenti, senza usarle per inventare ciò che è stato svolto. Affermazioni centrali senza supporto, riferimenti/risultati inventati e contraddizioni sostanziali impediscono di dichiarare il lavoro finale. Una bozza incompleta viene qualificata come tale. Ogni controllo finale identifica il file e la revisione esaminati; se il revisore distinto non è disponibile, il controllo del coordinatore viene dichiarato e la revisione indipendente richiesta resta pendente. [Criteri operativi](../skills/galileo/references/quality-gates.md).

Per una presentazione completa, Galileo supporta loghi, colori, font e template del gruppo di ricerca o dell’università, oppure propone stili adatti al pubblico, definisce palette e layout comuni e controlla due slide campione prima di completare il deck. Le slide campione fanno parte del numero richiesto. Una richiesta di solo testo o note salta questa fase grafica.

## Riprendi il lavoro

Richiama Galileo con la modalità prevista dal tuo client, nello stesso progetto, e scrivi:

```text
Continua dallo stato salvato in research_workspace/. Riutilizza le risposte già date.
```

Se ci sono più lavori compatibili, ti chiederà quale riprendere.

## Installa una volta

Dal repository, con Python 3.10+, scegli **un solo** comando in base al client e sostituisci il percorso del progetto:

```bash
# Claude Code
python3 scripts/install.py --dest "/percorso/del/progetto/.claude/skills"

# Codex
python3 scripts/install.py --dest "/percorso/del/progetto/.agents/skills"

# OpenCode
python3 scripts/install.py --dest "/percorso/del/progetto/.opencode/skills"

# GitHub Copilot
python3 scripts/install.py --dest "/percorso/del/progetto/.github/skills"
```

Il profilo completo è quello predefinito. Aggiungi `--dry-run` per vedere il piano senza scrivere file. L'installer non sovrascrive skill già presenti: per aggiornare o scegliere un altro client, segui la [guida di installazione](INSTALLATION.md). Dopo l'installazione aggiorna l'elenco delle skill o apri una nuova sessione nel progetto corretto.

## Agenti e portabilità

Per richiedere agenti separati puoi aggiungere:

```text
Usa Galileo in modalità agentica. Delega i ruoli pertinenti ad agenti separati,
se il client lo permette, e coordina revisioni e correzioni.
```

Gli agenti indipendenti richiedono supporto e autorizzazione del client. Altrimenti i ruoli vengono svolti in sequenza e il limite viene dichiarato. L'installazione non aggiunge definizioni native di agenti né garantisce il parallelismo.

La scelta dei modelli dipende dal tuo ambiente: gli esempi sono indicativi e non obbligano a usare un provider. Quando una ricerca bibliografica può beneficiare di una connessione non disponibile, Galileo propone gli MCP pertinenti e ti offre di configurarli oppure continuare con le fonti disponibili. Può anche cercare MCP pertinenti oltre al catalogo incluso, verificando la documentazione degli autori e distinguendo i candidati dalle integrazioni del pacchetto. Ricorda la scelta nelle riprese del lavoro. La proposta non attiva servizi: MCP, strumenti per documenti ed esportazioni richiedono configurazioni specifiche. I metadati dell'interfaccia Codex possono essere ignorati dagli altri client.

I controlli del pacchetto e gli esercizi sintetici sono descritti nella [revisione della release](RELEASE_REVIEW.md) e nel [report di usabilità](USABILITY_TESTS.md). Non sono ancora stati verificati workflow completi su Claude Code, OpenCode e GitHub Copilot.

Puoi installare il profilo completo oppure `core`, `docx`, `latex`, `slides`, `publishing`, `defense` o `systematic`. Ogni profilo include Galileo e gli strumenti di progetto; le skill vengono attivate in base al compito, non tutte insieme.

Le funzioni avanzate restano disponibili: [workflow e diagrammi](WORKFLOW_GUIDE.md), [formati](FORMATS_AND_SLIDES.md), [ricerca bibliografica MCP](LITERATURE_INTEGRATIONS.md) e [strumenti di progetto](PROJECT_TOOLS.md). Non occorre configurarli tutti per iniziare.

La revisione editoriale resta una simulazione; Galileo non invia nulla alle riviste. Capacità effettive e strumenti dipendono dal client: eventuali verifiche o esportazioni non eseguite restano indicate come tali. Per materiale riservato va prima definito il trattamento autorizzato.

Per una tesi completa, Galileo collega gli obiettivi alle sezioni, al contributo effettivo dell’autore e alle prove disponibili. Prima di ampliare ogni capitolo controlla che ci siano le spiegazioni necessarie, non soltanto titoli o schermate. La bibliografia viene valutata per copertura, pertinenza e corrispondenza con le citazioni in entrambe le direzioni, senza un numero minimo artificiale di articoli. Lacune centrali e revisioni riferite a versioni precedenti restano aperte; lo stato operativo «completato» non equivale alla prontezza scientifica.
