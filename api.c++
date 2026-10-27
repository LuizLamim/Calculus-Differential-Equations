#include "crow.h"

int main(){
    crow::SimpleApp app;

    CROW_ROUTE(app, "/api/aspectos")([](){
        crow::json::wvalue resposta;
        
        resposta["entidade"] = "Nome da Entidade";
        resposta["descricao"] = "Descrição breve sobre o tema.";
        resposta["principais_aspectos"] = std::vector<std::string>{
            "Aspecto fundamental 1", 
            "Aspecto fundamental 2", 
            "Aspecto fundamental 3"
        };
}