using Xamarin.Forms;
using StudentsApp.Views;

namespace StudentsApp
{
    public partial class App : Application
    {
        public App()
        {
            MainPage = new NavigationPage(new StudentsListPage());
        }

        protected override void OnStart()
        { }

        protected override void OnSleep()
        { }

        protected override void OnResume()
        { }
    }
}