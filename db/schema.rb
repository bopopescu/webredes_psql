# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2019_04_23_162911) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "acercades", force: :cascade do |t|
    t.text "descripcion"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "mision"
    t.string "vision"
    t.string "valores"
    t.bigint "user_id"
    t.index ["user_id"], name: "index_acercades_on_user_id"
  end

  create_table "avisos", force: :cascade do |t|
    t.string "titulo"
    t.text "detalle"
    t.datetime "fecha"
    t.string "imagen"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.index ["user_id"], name: "index_avisos_on_user_id"
  end

  create_table "doc_reconocimientos", force: :cascade do |t|
    t.string "titulo"
    t.text "contenido"
    t.bigint "user_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user_id"], name: "index_doc_reconocimientos_on_user_id"
  end

  create_table "eventos", force: :cascade do |t|
    t.string "titulo"
    t.string "detalle"
    t.string "lugar"
    t.datetime "fecha_inicio"
    t.datetime "fecha_fin"
    t.string "expositor"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "imagen"
    t.bigint "user_id"
    t.index ["user_id"], name: "index_eventos_on_user_id"
  end

  create_table "precios", force: :cascade do |t|
    t.string "plan"
    t.string "descripcion"
    t.float "precio"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.index ["user_id"], name: "index_precios_on_user_id"
  end

  create_table "recursos", force: :cascade do |t|
    t.string "nombre"
    t.string "user"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.index ["user_id"], name: "index_recursos_on_user_id"
  end

  create_table "servicios", force: :cascade do |t|
    t.string "nombre"
    t.text "caracteristicas"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.index ["user_id"], name: "index_servicios_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "nombre"
    t.string "appaterno"
    t.string "rfc"
    t.string "razon_social"
    t.string "domicilio_fiscal"
    t.string "domicilio_fisico"
    t.string "sucursal"
    t.string "telefono_oficina"
    t.string "nombre_enlace"
    t.string "appaterno_enlace"
    t.string "apmaterno_enlace"
    t.string "cargo_enlace"
    t.string "correo_enlace"
    t.string "telefono_enlace"
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.integer "sign_in_count", default: 0, null: false
    t.datetime "current_sign_in_at"
    t.datetime "last_sign_in_at"
    t.inet "current_sign_in_ip"
    t.inet "last_sign_in_ip"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "permission_level", default: 0, null: false
    t.string "type"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "acercades", "users"
  add_foreign_key "avisos", "users"
  add_foreign_key "doc_reconocimientos", "users"
  add_foreign_key "eventos", "users"
  add_foreign_key "precios", "users"
  add_foreign_key "recursos", "users"
  add_foreign_key "servicios", "users"
end
