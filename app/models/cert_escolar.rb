class CertEscolar < ApplicationRecord
	include PgSearch::Model

	has_many_attached :evidencias

  enum status: {sin_avance: 0, desarrollo: 1, revision: 2, comentarios: 3, cumplido: 4}

  before_update do |proceso| 
  	validates_presence_of :observaciones
  	validates_numericality_of :puntaje, greater_than_or_equal_to: 0
  end

  pg_search_scope :search_by_full_escuela, associated_against: { escuela: [ :nombre, :razon_social] }, 
  					using:   {tsearch: { prefix: true }},
  					order_within_rank: " paso ASC,  estandar ASC"

	def det_estandar(paso_id, estandar_id)
    @estandar = EstandarEtapaCertificacion.find_by(num_etapa: paso_id, num_estandar: estandar_id)
  end
 
  def det_paso(paso_id)
    @paso = EtapaCertificacion.find_by(num_paso: paso_id)
  end

  def det_puntos(estandar_id)
    @puntos = PuntosEstandar.where(estandar_etapa_certificacion_id: estandar_id)
  end

	def puntos_objetivo
		puntos_totales_estandar = EstandarEtapaCertificacion.find_by(num_etapa: self.paso, num_estandar: self.estandar).puntaje_total 
		return puntos_totales_estandar
	end  

  def nombre_escuela
    nombre_escuela = Escuela.where(id: self.escuela_id).first.nombre
  end					

end

 