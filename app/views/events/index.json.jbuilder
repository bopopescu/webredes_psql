#json.array! @events, partial: 'events/event', as: :evento

json.array! @events do |event|
  date_format = event.all_day_event? ? '%Y-%m-%d' : '%Y-%m-%dT%H:%M:%S'
  json.id event.id
  json.title event.titulo
  json.start event.start.strftime(date_format)
  json.end event.end.strftime(date_format)
  json.color event.color unless event.color.blank?
  json.allDay event.all_day_event? ? true : false
  json.detalle event.detalle
  json.foto event.foto
  json.update_url event_path(event, method: :patch)
  json.edit_url edit_event_path(event)
  json.show_url event_path(event)
end
