# Guida italiana

Questo pacchetto è generico: tesi, dottorati, articoli e rapporti scientifici di discipline e paesi diversi. Le istruzioni principali sono in inglese, ma puoi chiedere l'output in italiano o un'altra lingua.

Installa dal repository con `python3 scripts/install.py --dest /percorso/progetto/.agents/skills`, preceduto da `--dry-run` per verificare il piano. Vengono copiate due skill di workflow e sette skill scientifiche, senza installare librerie o attivare servizi. Leggi [la guida principale](../README.md).

Nell'app Codex digita `/` e scegli Research drafting o Research review, se il client le mostra. Nel CLI usa `/skills`. In alternativa scrivi `$research-drafting` o `$research-review`, seguito dalla richiesta.

Stesura: domande progressive, fonti/scoring, analisi, bozza e audit. Revisione: fascicolo congelato, controlli editoriali, tre reviewer simulati, decisione, risposta e correzioni. Per riprendere chiedi di continuare dallo stato salvato.

Il profilo balanced usa modelli intermedi per la maggior parte del lavoro, economici per compiti di forma e un modello più capace per la revisione statistica e le escalation. I modelli sono esempi configurabili, non una dipendenza. I ruoli non sono reviewer umani e il processo non invia nulla a una rivista.

Questo pacchetto non contiene dati personali o materiali di una tesi specifica. L'utente resta responsabile delle decisioni scientifiche e delle autorizzazioni effettive.
