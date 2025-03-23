# Local-RAG
Local RAG with Chainlit GUI.

### What I used?
[Chainlit](https://docs.chainlit.io/get-started/overview) + [Embedchain](https://github.com/embedchain/embedchain/tree/main) + [Ollama](https://ollama.com/)

### Data
I imported data in forms of URLs that are embedded into LLM. Right now `sample_data.csv` contains only one resource, [A Cypherpunk's Manifesto](https://www.activism.net/cypherpunk/manifesto.html).

## Installation

The setup assumes you have `python` already installed.

1. Install [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#ollama), for Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Pull model from Ollama. Default model is `deepseek-r2:1.5B`
```bash
ollama pull deepseek-r2:1.5B
```

3. Open Terminal in Local-RAG folder

4. Install required packages
```bash
pip install -r requirements.txt
```

5. Start `ollama`:
```bash
ollama serve
```

6. Start `app.py`:
```bash
chainlit run app.py
```

7. Now you can prompt the AI.

## Changing Configuration

If you want to change the Large Language Model model or Embedding model, open `config.yaml`in your text editor or IDE.

Following code sets the configuration:

```bash
1 llm:
2	provider: ollama
3	config:
4	model: 'deepseek-r1:1.5b'
5	temperature: 0.5
6	top_p: 1
7	stream: true
8	base_url: 'http://localhost:11434'
9
10 embedder:
11	provider: ollama
12	config:
13	model: 'nomic-embed-text'
14	base_url: 'http://localhost:11434'
```

### Changing Large Language Model
You can change which Large Language Model is being use by changing the model in line 4. You can choose from [Ollama models](https://ollama.com/search). 

```bash
4   model: 'deepseek-r1:1.5b'
```

For further Large Language Models customization (another local solutions or APIs), see [Embedchain documentation](https://docs.embedchain.ai/components/llms).

### Changing Embedding Model
You can change which Embedding Model is being use by changing the model in line 13. You can choose from [Ollama models](https://ollama.com/search?c=embedding).

```bash
13  model: 'nomic-embed-text'
```

For further Embedding Models customization (another local solutions or APIs), see [Embedchain documentation](https://docs.embedchain.ai/components/embedding-models).

## Changing Embedded Data
If you want to change the embedded data, open `sample_data.csv`in your text editor or IDE.

Now you can add your URLs or other data.

For further customization of embedded data, see [Embedchain customization](https://docs.embedchain.ai/get-started/quickstart). 
