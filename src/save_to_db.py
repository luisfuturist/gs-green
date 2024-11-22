from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from db_config import SessionLocal, engine
from models import Base, EnergyConsumption

# Create tables
Base.metadata.create_all(bind=engine)

def save_data_to_db(data):
    session = SessionLocal()
    try:
        for record in data:
            # Ensure 'dat_competencia' is a valid date
            dat_competencia = record["DatCompetencia"]
            if isinstance(dat_competencia, str):
                try:
                    # Parse the date string into a datetime object
                    dat_competencia = datetime.strptime(dat_competencia, "%Y-%m-%d").date()
                except ValueError:
                    print(f"Invalid date format: {dat_competencia}")
                    continue  # Skip this record if the date is invalid
            
            dat_geracao_conjunto_dados = record["DatGeracaoConjuntoDados"]
            if isinstance(dat_geracao_conjunto_dados, str):
                try:
                    # Parse the date string into a datetime object
                    dat_geracao_conjunto_dados = datetime.strptime(dat_geracao_conjunto_dados, "%Y-%m-%d").date()
                except ValueError:
                    print(f"Invalid date format: {dat_geracao_conjunto_dados}")
                    continue

            vlrMercado = record["VlrMercado"]
            if isinstance(vlrMercado, str):
                try:
                    value_corrected = vlrMercado.replace(",", ".")
                    # Parse the date string into a datetime object
                    vlrMercado = float(value_corrected)
                except ValueError:
                    print(f"Invalid date format: {vlrMercado}")
                    continue

            entry = EnergyConsumption(
                dat_geracao_conjunto_dados=dat_geracao_conjunto_dados,
                num_cnpj_agente_distribuidora=record["NumCNPJAgenteDistribuidora"],
                sig_agente_distribuidora=record["SigAgenteDistribuidora"],
                nom_agente_distribuidora=record["NomAgenteDistribuidora"],
                nom_tipo_mercado=record["NomTipoMercado"],
                dsc_modalidade_tarifaria=record["DscModalidadeTarifaria"],
                dsc_sub_grupo_tarifario=record["DscSubGrupoTarifario"],
                dsc_classe_consumo_mercado=record["DscClasseConsumoMercado"],
                dsc_sub_classe_consumidor=record["DscSubClasseConsumidor"],
                dsc_detalhe_consumidor=record["DscDetalheConsumidor"],
                ide_agente_acessante=record["IdeAgenteAcessante"],
                num_cnpj_agente_acessante=record["NumCNPJAgenteAcessante"],
                nom_agente_acessante=record["NomAgenteAcessante"],
                dsc_posto_tarifario=record["DscPostoTarifario"],
                dsc_opcao_energia=record["DscOpcaoEnergia"],
                dsc_classificacao=record["DscClassificacao"],
                dsc_detalhe_mercado=record["DscDetalheMercado"],
                dat_competencia=dat_competencia,  # Use the correctly formatted date
                vlr_mercado=vlrMercado
            )
            session.add(entry)
        session.commit()
    except SQLAlchemyError as e:
        print(f"Error saving data: {e}")
        session.rollback()
    finally:
        session.close()
