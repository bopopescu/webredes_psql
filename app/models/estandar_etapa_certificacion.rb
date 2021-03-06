class EstandarEtapaCertificacion < ApplicationRecord
    before_destroy :no_referenced_puntos_estandars 
	
	belongs_to :etapa_certificacion
	belongs_to :proceso 
	 
	has_many :puntos_estandars, :dependent => :destroy 

	validates_presence_of :titulo, :descripcion, :observaciones, :evidencias, :etapa_certificacion_id, :puntaje_total, :num_estandar
  
  	validates_uniqueness_of :num_estandar, :scope => [:etapa_certificacion_id, :proceso_id]

	accepts_nested_attributes_for :puntos_estandars, reject_if: :all_blank, allow_destroy: true

	has_many_attached :obligatorio
	has_many_attached :apoyo

	before_create  do
		self.num_etapa = self.etapa_certificacion.num_paso
	end
	
	attr_accessor :remove_obligatorio, :remove_apoyo
	
	 after_save do
	 	Array(remove_obligatorio).each { |id| obligatorio.find_by_id(id).try(:purge) }
	 	Array(remove_apoyo).each { |id| apoyo.find_by_id(id).try(:purge) }
	 end

	def nombre_archivo(archivo) 
		nombre_archivo = archivo.filename 
	end

	def no_referenced_puntos_estandars
    	return if puntos_estandars.empty?
    	errors.add :base,  "No se permite hay ..."
    	false # If you return anything else, the callback will not stop the destroy from happening
  	end

  	def titulo_modelo
  		self.titulo.truncate(25) + '...' if !titulo.blank?
  	end

  	def periodo
  		periodo = Proceso.where(id: proceso_id).first.periodo
  	end
 
end


 


