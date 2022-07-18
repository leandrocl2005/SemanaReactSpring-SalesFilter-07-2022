import { toast } from 'react-toastify';
import icon from '../../assets/img/notification_icon.svg'
import './styles.css'

type Props = {
    saleId: number;
}

function handleClick(id: Number) {
    toast.info("SMS Enviado com sucesso")
}


function NotificationButton({saleId}: Props) {

    return (
        <div className="dsmeta-red-btn" onClick={() => handleClick(saleId)}>
            <img src={icon} alt="Notificar" />
        </div>
    )
}
export default NotificationButton