using Akka.Actor;

namespace NaruNet
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Creando Sistema de Actores
            ActorSystem MyActorSystem = ActorSystem.Create("MyActorSystem");

            //Creando Actores
            IActorRef consoleWriter = MyActorSystem.ActorOf(Props.Create<ConsoleWriter>());
            IActorRef user1 = MyActorSystem.ActorOf(Props.Create(() => new User(consoleWriter)), "Shikamaru");
            IActorRef user2 = MyActorSystem.ActorOf(Props.Create(() => new User(consoleWriter)), "Naruto");
            IActorRef user3 = MyActorSystem.ActorOf(Props.Create(() => new User(consoleWriter)), "Kakashi");
            IActorRef user4 = MyActorSystem.ActorOf(Props.Create(() => new User(consoleWriter)), "Gaara");
            IActorRef user5 = MyActorSystem.ActorOf(Props.Create(() => new User(consoleWriter)), "Kabuto");

            //Enviando mensajes
            user2.Tell(new Actions.SendMessage("Hola qué tal"), user1);
            user1.Tell(new Actions.SendMessage("Muy bien, gracias"), user2);
            user2.Tell(new Actions.SendMessage("Es hora de entrenar, Naruto"), user3);
          

            //Publicando Posts
            user2.Tell(new Actions.SendPost("SERÉ HOKAGE, pues ese es mi camino ninja DATEBAYOU"));
            user1.Tell(new Actions.SendPost("Si tan solo fuese una nube"));
           

            //Siguiendo usuarios
            user2.Tell(new Actions.FollowUser(user1));
            user2.Tell(new Actions.FollowUser(user4));
            user2.Tell(new Actions.FollowUser(user5));
            user1.Tell(new Actions.FollowUser(user2));
            user1.Tell(new Actions.FollowUser(user4));
            user4.Tell(new Actions.FollowUser(user3));
            user4.Tell(new Actions.FollowUser(user5));
           

            //Mostrar lista de seguidores
            user2.Tell(new Actions.GetFollowers());
            user4.Tell(new Actions.GetFollowers());

            //Mostrar lista de usuarios seguidos
            user2.Tell(new Actions.GetFollowedUsers());
            user1.Tell(new Actions.GetFollowedUsers());
            

            MyActorSystem.Terminate().Wait();

        }
    }
}