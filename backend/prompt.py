from langchain.prompts import PromptTemplate

template = """Verilen bağlama dayalı olarak soruya yanıt verin. Bağlam ve soru aşağıda verilmiştir. Eğer soru bağlamı ile ilgili değilse, " Bu sorunun cevabı \
bilmiyorum" yazın. Ilgili ise bağlamı okuyun ve soruyu ayrıntılı bir şekilde cevaplayın.

Bağlam: {context}

Soru: {question}

Cevap: """

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=template,

)

# p = prompt_template.format(context="The president", question="Who is the president?")
