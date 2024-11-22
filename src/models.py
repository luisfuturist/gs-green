from sqlalchemy import Column, String, Integer, DECIMAL, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class EnergyConsumption(Base):
    __tablename__ = "energy_consumption"
    
    id = Column(Integer, primary_key=True, index=True)
    dat_geracao_conjunto_dados = Column(Date, nullable=False)
    num_cnpj_agente_distribuidora = Column(String, nullable=False)
    sig_agente_distribuidora = Column(String, nullable=False)
    nom_agente_distribuidora = Column(String, nullable=False)
    nom_tipo_mercado = Column(String, nullable=False)
    dsc_modalidade_tarifaria = Column(String)
    dsc_sub_grupo_tarifario = Column(String)
    dsc_classe_consumo_mercado = Column(String)
    dsc_sub_classe_consumidor = Column(String)
    dsc_detalhe_consumidor = Column(String)
    ide_agente_acessante = Column(String)
    num_cnpj_agente_acessante = Column(String)
    nom_agente_acessante = Column(String)
    dsc_posto_tarifario = Column(String)
    dsc_opcao_energia = Column(String)
    dsc_classificacao = Column(String)
    dsc_detalhe_mercado = Column(String)
    dat_competencia = Column(Date, nullable=False)
    vlr_mercado = Column(DECIMAL(15, 6))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
