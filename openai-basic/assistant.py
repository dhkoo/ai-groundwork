from openai import OpenAI
from dotenv import load_dotenv
import os

from dotenv import load_dotenv

load_dotenv()

class OpenAIAssistant:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
    
    def createAssistant(self, name: str, instructions: str):
        assistant = self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=[{"type": "code_interpreter"}, {"type": "retrieval"}],
            model="gpt-4-1106-preview"
        )
        print(assistant.id)

    # A Thread represents a conversation.
    # Threads don’t have a size limit. You can pass as many Messages as you want to a Thread. 
    def createThread(self):
        thread = self.client.beta.threads.create()
        print(thread.id)
        return thread.id
    
    def createMessage(self, thread_id: str, content: str, file_id: str= None):
        message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content,
            file_ids=[file_id]
        )
        print(message.id)
        return message.id

    def run(self, thread_id: str ,assistant_id: str):
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )
        print(run.id)
        return run.id
    
    def checkRunStatus(self, run_id: str, thread_id: str):
        status = self.client.beta.threads.runs.retrieve(
            run_id=run_id,
            thread_id=thread_id
        )
        print(status.status)
        return status
    
    def checkResult(self, thread_id: str):
        messages = self.client.beta.threads.messages.list(
            thread_id=thread_id
        )
        value = messages.data[0].content[0].text.value
        print(value)
        return value
    
    def checkMessage(self, thread_id: str, message_id: str):
        message = self.client.beta.threads.messages.retrieve(
            thread_id=thread_id,
            message_id=message_id
        )
        print(message)
        message_content = message.content[0].text
        print(message_content)
    

def test():
    api_key = os.getenv("OPENAI_API_KEY")
    oa = OpenAIAssistant(api_key)

    # oa.createAssistant("Arit", "Arit is a friendly AI assistant that helps you with your daily tasks.")
    assistant_id = "asst_Y0i9AIz1ITMYQ0cuxvUJKOKT"

    # oa.createThread()
    thread_id = "thread_bO7i7LLUCzf9LFh9fPfPvByH"

    # oa.createMessage(thread_id, "아침 루틴을 만들고 싶어. 추천해줘.")
    message_id = "msg_NAoQZ2IcviiBo794GYp1RSDN"

    # oa.run(thread_id, assistant_id)

    oa.checkResult(thread_id)
    # oa.checkMessage(thread_id, message_id)

def test2():
    api_key = os.getenv("OPENAI_API_KEY")
    oa = OpenAIAssistant(api_key)

    assistant_id = "asst_kMNkTV4bbjqwTtjcsiFtfkJQ"
    # oa.createThread()
    thread_id = "thread_vMXfDIPuoPopxMb3h5ILWw8P"

    # oa.createMessage(thread_id, "첨부한 파일의 '일광' 캐릭터 분석해줘" , "file-Yv6na3bixouCcD5v99GZn6Gj")
    message_id = "msg_wlG3duEtgnW17GGExUeLA0v5"

    # oa.run(thread_id, assistant_id)
    # oa.checkRunStatus("run_ZYtg08aB7iv4DEbRnYXUPEFA", thread_id)
    oa.checkResult(thread_id)


if __name__ == "__main__":
    test2()
