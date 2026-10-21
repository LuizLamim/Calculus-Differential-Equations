package com.exemplo.api.controller;

import com.exemplo.api.model.Item;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/itens")
public class ItemController {

    private final List<Item> itens = new ArrayList<>();

    public ItemController() {
        itens.add(new Item(1L, "Item A"));
        itens.add(new Item(2L, "Item B"));
    }

    // GET: Retorna todos os itens
    @GetMapping
    public List<Item> listarTodos() {
        return itens;
    }

    // GET: Retorna um item pelo ID
    @GetMapping("/{id}")
    public ResponseEntity<Item> buscarPorId(@PathVariable Long id) {
        return itens.stream()
                .filter(item -> item.getId().equals(id))
                .findFirst()
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // POST: Adiciona um novo item
    @PostMapping
    public ResponseEntity<Item> criar(@RequestBody Item novoItem) {
        itens.add(novoItem);
        return ResponseEntity.status(HttpStatus.CREATED).body(novoItem);
    }
}