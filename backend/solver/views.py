from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.control import SolverController
from .services.history import HistoryService

class SolveEquationView(APIView):
    def post(self, request):
        try:
            result = SolverController.solve_system(request.data)
            return Response(result, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HistoryListView(APIView):
    def get(self, request):
        try:
            history = HistoryService.get_history()
            return Response(history, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HistoryDetailView(APIView):
    def get(self, request, pk):
        try:
            attempt = HistoryService.get_attempt(pk)
            if attempt:
                return Response(attempt, status=status.HTTP_200_OK)
            return Response({"error": "Attempt not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
