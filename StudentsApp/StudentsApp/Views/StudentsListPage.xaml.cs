using Xamarin.Forms;
using StudentsApp.ViewModels;

namespace StudentsApp.Views
{
    public partial class StudentsListPage : ContentPage
    {
        public StudentsListPage()
        {
            InitializeComponent();
            BindingContext = new StudentsListViewModel() { Navigation = this.Navigation };
        }
    }
}