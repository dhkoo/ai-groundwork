def read_prompt_template(file_path: str) -> str:
    prompt_template = ""
    with open(file_path, "r") as f:
        prompt_template = f.read()

    return prompt_template

