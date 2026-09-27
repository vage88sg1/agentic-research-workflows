# Galileo — Guida rapida

**Descrivi cosa vuoi ottenere. Galileo sceglie il percorso e ti accompagna nel lavoro.**

Dopo l'installazione, digita `/` in un client Codex desktop compatibile e scegli **Galileo**. Nel CLI usa `/skills`; in alternativa puoi scrivere `$galileo` seguito dalla richiesta. Non serve imparare i nomi dei workflow o compilare file di configurazione.

## Parti da una richiesta semplice

```text
$galileo Aiutami a scrivere la mia tesi. Ho la descrizione dello studio e i risultati
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

## Riprendi il lavoro

Seleziona di nuovo Galileo nello stesso progetto e scrivi:

```text
Continua dallo stato salvato in research_workspace/. Riutilizza le risposte già date.
```

Se ci sono più lavori compatibili, ti chiederà quale riprendere.

## Installa una volta

Dal repository, con Python 3.10+:

```bash
python3 scripts/install.py --dest /percorso/del/progetto/.agents/skills
```

Il profilo completo è quello predefinito. Aggiungi `--dry-run` per vedere il piano senza scrivere file. L'installer non sovrascrive skill già presenti: per aggiornare o scegliere un altro client, segui la [guida di installazione](INSTALLATION.md). Dopo l'installazione aggiorna l'elenco delle skill o apri una nuova sessione nel progetto corretto.

Le funzioni avanzate restano disponibili: [workflow e diagrammi](WORKFLOW_GUIDE.md), [formati](FORMATS_AND_SLIDES.md), [ricerca bibliografica MCP](LITERATURE_INTEGRATIONS.md) e [strumenti di progetto](PROJECT_TOOLS.md). Non occorre configurarli tutti per iniziare.

La revisione editoriale resta una simulazione; Galileo non invia nulla alle riviste. Capacità effettive e strumenti dipendono dal client: eventuali verifiche o esportazioni non eseguite restano indicate come tali. Per materiale riservato va prima definito il trattamento autorizzato.
