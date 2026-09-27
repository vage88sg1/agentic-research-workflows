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

Il profilo completo contiene **Galileo, nove workflow specialistici e nove skill di supporto: 19 cartelle di skill**.

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
| Tracciabilità e riproducibilità | Quattro comandi offline: `preflight`, `evidence`, `impact` e `bundle`; dipendenze registrate, hash e file selezionati |
| Qualità e costo | Profili di costo configurabili, contesti mirati, riuso delle evidenze e modelli disponibili nel proprio client |

Sono istruzioni di workflow e strumenti locali: agenti indipendenti, ricerche, calcoli, esportazioni e controlli visivi dipendono dalle capacità reali del client. I risultati non eseguiti non vengono dichiarati completati.

## Scegli il percorso

Non serve imparare i nomi: descrivi l'obiettivo a Galileo. Puoi anche richiamare direttamente questi workflow:

| Workflow | Obiettivo |
|---|---|
| Research drafting | Scrivere o migliorare tesi e articoli |
| Research review | Simulare peer review, decisione e correzioni |
| Research typesetting | Produrre Word, LaTeX e PDF |
| Research presentations | Preparare e revisionare slide scientifiche |
| Research project | Controllare evidenze, cambiamenti e riproducibilità |
| Thesis to article | Convertire una tesi in un articolo mirato |
| Research defense | Allenarsi alla discussione e alle domande |
| Submission dossier | Preparare i materiali richiesti dalla rivista |
| Systematic review | Svolgere una revisione sistematica esplicitamente richiesta |

[Guida completa con esempi e un diagramma per ogni workflow](WORKFLOW_GUIDE.md).

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

Galileo usa le informazioni già disponibili, fa le domande necessarie e attiva le competenze pertinenti. Quando serve produrre il documento, chiarisce Word o LaTeX. Mantiene nei registri del progetto evidenze, controlli e problemi aperti. Non devi rilanciare un comando per ogni passaggio di un lavoro già richiesto.

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
