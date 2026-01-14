min_quarter = '2016 Q1'
min_quarter_plot = '2020 Q1'
max_quarter = '2025 Q1'
max_count = 40000

repos_frameworks = [
    'huggingface/accelerate',
    'awslabs/multi-model-server',
    'bentoml/BentoML',
    'huggingface/candle',
    'neuralmagic/deepsparse',
    'microsoft/DeepSpeed',
    'deepspeedai/DeepSpeed-MII',
    'ai-dynamo/dynamo',
    'pytorch/executorch',
    'turboderp/exllamav2',
    'ggerganov/llama.cpp',
    'InternLM/lmdeploy',
    'ROCm/AMDMIGraphX',
    'EricLBuehler/mistral.rs',
    'mlc-ai/mlc-llm',
    'alibaba/MNN',
    'microsoft/onnxruntime',
    'openvinotoolkit/openvino',
    'robertknight/rten',
    'sgl-project/sglang',
    'NVIDIA/TensorRT-LLM',
    'NVIDIA/TensorRT',
    'tensorflow/serving',
    'huggingface/text-generation-inference',
    'pytorch/serve',
    'triton-inference-server/server',
    'vllm-project/vllm',
    'ollama/ollama',
]

repos_langs = [
    'microsoft/CNTK',
    'google/jax',
    'keras-team/keras',
    'mindspore-ai/mindspore',
    'dotnet/machinelearning',
    'ml-explore/mlx',
    'apache/mxnet',
    'PaddlePaddle/Paddle',
    'plaidml/plaidml',
    'pytorch/pytorch',
    'tensorflow/tensorflow',
    'tinygrad/tinygrad',
    'triton-lang/triton',
    'modular/mojo',
    'NVIDIA/cutlass',
    'HazyResearch/ThunderKittens',
    'tile-ai/tilelang',
    'openxla/xla',
    'apache/tvm',
    'ROCm/HIP',
]

repos_models = [
    'google-research/bert',
    'databricks/dbrx',
    'deepseek-ai/DeepSeek-R1',
    'deepseek-ai/DeepSeek-V2',
    'deepseek-ai/DeepSeek-V3',
    'openai/gpt-2',
    'xai-org/grok-1',
    'meta-llama/llama',
    'meta-llama/llama3',
    'mistralai/mistral-inference',
    'microsoft/PhiCookBook',
    'QwenLM/Qwen2.5',
]

repos = repos_frameworks + repos_langs + repos_models
