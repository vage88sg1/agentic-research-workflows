# Galileo: Agentic Research Workflows — Guida italiana

Questo pacchetto è generico: tesi, dottorati, articoli e rapporti scientifici di discipline e paesi diversi. Le istruzioni principali sono in inglese, ma puoi chiedere l'output in italiano o un'altra lingua.

Installa dal repository con `python3 scripts/install.py --dest /percorso/progetto/.agents/skills`, preceduto da `--dry-run` per verificare il piano. Il profilo completo copia nove voci di workflow e nove skill di supporto, senza installare librerie o attivare servizi. Puoi scegliere `--profile core`, `docx`, `latex`, `slides`,  `publishing`, `defense`, `systematic` o `full`. Leggi [la guida principale](../README.md).

Nell'app Codex digita `/` e scegli Research drafting o Research review, se il client le mostra. Nel CLI usa `/skills`. In alternativa scrivi `$research-drafting` o `$research-review`, seguito dalla richiesta.

Stesura: domande progressive, fonti/scoring, analisi, bozza e audit. Revisione: fascicolo congelato, controlli editoriali, tre reviewer simulati, decisione, risposta e correzioni. Per riprendere chiedi di continuare dallo stato salvato.

Il profilo balanced usa modelli intermedi per la maggior parte del lavoro, economici per compiti di forma e un modello più capace per la revisione statistica e le escalation. I modelli sono esempi configurabili, non una dipendenza. I ruoli non sono reviewer umani e il processo non invia nulla a una rivista.

Questo pacchetto non contiene dati personali o materiali di una tesi specifica. L'utente resta responsabile delle decisioni scientifiche e delle autorizzazioni effettive.

Scegli DOCX o LaTeX durante la stesura; la guida LaTeX si attiva solo per quel formato. Research typesetting gestisce impaginazione, compilazione/export e controllo visivo. Research presentations crea un piano delle slide, PPTX modificabile e PDF della stessa versione con revisione scientifica, visuale e della durata. Il solo PDF può anche usare Beamer; non promette una conversione automatica in PowerPoint modificabile.

## MCP opzionali per la letteratura

Il pacchetto include configurazioni per PubMed/Europe PMC, OpenAlex, Crossref e un adattatore Zotero sperimentale. In Codex sono inizialmente disattivati; negli altri client i frammenti JSON sono da importare singolarmente con i permessi appropriati. L'installer delle skill non li attiva. La [guida MCP](LITERATURE_INTEGRATIONS.md) spiega requisiti, credenziali opzionali, registro delle ricerche, limiti di costo e controlli di connessione. Per Zotero va controllata anche la configurazione di avvio, che può attivare indicizzazione o embeddings.

## Nuove funzioni

Ogni profilo include **Research project**: verifica preliminare delle capacità, mappa affermazioni–evidenze, analisi degli effetti delle modifiche e pacchetto di riproducibilità con file selezionati. I controlli automatici verificano struttura e file; il significato scientifico delle fonti richiede una valutazione distinta. La [guida degli strumenti](PROJECT_TOOLS.md) include un esempio sintetico eseguibile.

- **Thesis to article** trasforma una tesi in un articolo con mappa delle sezioni e controllo delle omissioni.
- **Research defense** simula domande della commissione, attende le risposte reali e fornisce feedback.
- **Submission dossier** prepara i materiali locali per una rivista e raccoglie dichiarazioni autentiche; il fascicolo resta NOT SUBMITTED.
- **Systematic review** gestisce protocollo, ricerca, screening, estrazione, valutazione e sintesi, distinguendo attività AI e umane e lasciando visibili le fasi incomplete.

Dal menu `/` scegli la voce disponibile; in alternativa usa `$research-project`, `$research-thesis-to-article`, `$research-defense`, `$research-submission` o `$research-systematic-review`. Il [README](../README.md) mostra i percorsi e i diagrammi separati.
