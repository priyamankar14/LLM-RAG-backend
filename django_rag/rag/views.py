

#new for ollama




# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rag.retriever import retrieve
# from rag.llm import generate_answer


# @api_view(["POST"])
# def ask(request):
#     question = request.data.get("question")

#     if not question:
#         return Response({"error": "Question is required"}, status=400)

#     # 1️⃣ Retrieve relevant documents
#     results = retrieve(question)

#     if not results:
#         return Response(
#             {"answer": "No relevant documents found."},
#             status=200
#         )

#     # 2️⃣ Combine context
#     context = "\n".join([r["content"] for r in results])

#     # 3️⃣ Generate final answer using Ollama
#     answer = generate_answer(context, question)

#     return Response({
#         "question": question,
#         "answer": answer
#     })









from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rag.retriever import retrieve
from rag.llm import generate_answer


@api_view(["POST"])
def ask(request):
    question = request.data.get("question")

    if not question:
        return Response(
            {"error": "Question is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # 1️⃣ Retrieve documents
        docs = retrieve(question)

        if not docs:
            return Response({
                "answer": "No relevant documents found."
            })

        # 2️⃣ Build context
        context = "\n".join([d["content"] for d in docs])

        # 3️⃣ Generate answer
        answer = generate_answer(context, question)

        return Response({
            "question": question,
            "answer": answer
        })

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
