class EventosController < ApplicationController
  before_action :set_evento, only: [:show, :edit, :update, :destroy]

  def index
    @eventos = Evento.all
  end

  def show
    authorize @evento
  end

  def new
    @evento = Evento.new
  end

  def edit
    authorize @evento
  end

  def create
  #  @evento = Evento.new(evento_params)
     @evento = current_user.eventos.new(evento_params)

    respond_to do |format|
      if @evento.save
        format.html { redirect_to @evento, notice: 'Evento was successfully created.' }
        format.json { render :show, status: :created, location: @evento }
      else
        format.html { render :new }
        format.json { render json: @evento.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    authorize @evento

    respond_to do |format|
      if @evento.update(evento_params)
        format.html { redirect_to @evento, notice: 'Evento was successfully updated.' }
        format.json { render :show, status: :ok, location: @evento }
      else
        format.html { render :edit }
        format.json { render json: @evento.errors, status: :unprocessable_entity }
      end
    end
  end

  def destroy
    @evento.destroy
    respond_to do |format|
      format.html { redirect_to eventos_url, notice: 'Evento was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    def set_evento
      @evento = Evento.find(params[:id])
    end

    def evento_params
      params.require(:evento).permit(:titulo, :detalle, :lugar, :fecha_inicio, :fecha_fin, :expositor, :imagen, :user_id)
    end
end
