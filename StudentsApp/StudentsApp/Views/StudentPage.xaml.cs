using StudentsApp.ViewModels;
using Xamarin.Forms;

namespace StudentsApp.Views
{
    public partial class StudentPage : ContentPage
    {
        public StudentViewModel ViewModel { get; private set; }
        public StudentPage(StudentViewModel vm)
        {
            InitializeComponent();
            ViewModel = vm;
            this.BindingContext = ViewModel;
        }
    }
}