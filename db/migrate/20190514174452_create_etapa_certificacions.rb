class CreateEtapaCertificacions < ActiveRecord::Migration[5.2]
  def change
    create_table :etapa_certificacions do |t|
      t.text :nombre
      t.text :descripcion

      t.timestamps
    end
  end
end
