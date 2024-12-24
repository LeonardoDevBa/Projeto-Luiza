
                                    garagem = str(input("Informe para qual garagem: "))
                                    gar = repository.pesquisar_garagem(garagem)
                                    # Comparação correta de garagem
                                    if garagem.strip().lower() == gar.localizacao.strip().lower():
                                        while True:
                                            quantidade = str(input("Quantidade desejada: "))
                                            if quantidade.isnumeric():
                                                quantidade = float(quantidade)  # Convertendo para float
                                                dados = ['Funcionario:', funcionario.nome, 'Garagem:', gar.nome, 'Item:', cod_cod.nome, 'Qtd. Solicitada:', quantidade]
                                                
                                                # Certifique-se de que 'dados' seja uma string antes de criptografar
                                                dados_formatados = str(dados)  # Converte a lista para uma string
                                                dados_criptografados = criptografia(dados_formatados)  # Chama a criptografia com string formatada
                                                
                                                arquivo = "Historico.txt"
                                                criando_arquivo_final(arquivo, dados_criptografados)
                                                print("O item será entregue em breve!")
                                                print(dados_formatados)
                                                sleep(10)
                                            else:
                                                print("Somente números são aceitos!")
                                    else:
                                        print("Garagem não encontrada!")
                                else:
                                    break
                        case "2":
                            break
                        case "_":
                            print("Opção inválida!")
                            sleep(2)