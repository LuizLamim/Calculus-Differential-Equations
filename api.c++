#include "crow.h"

int main() {
    crow::SimpleApp app;

    // Rota GET para retornar os principais aspectos
    CROW_ROUTE(app, "/api/aspectos")([](){
        crow::json::wvalue resposta;
        
        resposta["entidade"] = "Nome da Entidade";
        resposta["descricao"] = "Descrição breve sobre o tema.";
        resposta["principais_aspectos"] = std::vector<std::string>{
            "Aspecto fundamental 1", 
            "Aspecto fundamental 2", 
            "Aspecto fundamental 3"
        };
        
        return resposta;
    });

    // Inicia o servidor na porta 8080
    app.port(8080).multithreaded().run();
}