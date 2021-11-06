using System.Collections.ObjectModel;
using System.Windows.Input;
using Xamarin.Forms;
using System.ComponentModel;
using StudentsApp.Views;

namespace StudentsApp.ViewModels
{
    public class StudentsListViewModel : INotifyPropertyChanged
    {
        public ObservableCollection<StudentViewModel> Students { get; set; }

        public event PropertyChangedEventHandler PropertyChanged;

        public ICommand CreateStudentCommand { protected set; get; }
        public ICommand DeleteStudentCommand { protected set; get; }
        public ICommand SaveStudentCommand { protected set; get; }
        public ICommand BackCommand { protected set; get; }
        StudentViewModel selectedStudent;

        public INavigation Navigation { get; set; }

        public StudentsListViewModel()
        {
            Students = new ObservableCollection<StudentViewModel>();
            CreateStudentCommand = new Command(CreateStudent);
            DeleteStudentCommand = new Command(DeleteStudent);
            SaveStudentCommand = new Command(SaveStudent);
            BackCommand = new Command(Back);
        }

        public StudentViewModel SelectedStudent
        {
            get { return selectedStudent; }
            set
            {
                if (selectedStudent != value)
                {
                    StudentViewModel tempStudent = value;
                    selectedStudent = null;
                    OnPropertyChanged("SelectedStudent");
                    Navigation.PushAsync(new StudentPage(tempStudent));
                }
            }
        }
        protected void OnPropertyChanged(string propName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propName));
        }

        private void CreateStudent()
        {
            Navigation.PushAsync(new StudentPage(new StudentViewModel() { ListViewModel = this }));
        }
        private void Back()
        {
            Navigation.PopAsync();
        }
        private void SaveStudent(object StudentObject)
        {
            StudentViewModel Student = StudentObject as StudentViewModel;
            if (Student != null && Student.IsValid && !Students.Contains(Student))
            {
                Students.Add(Student);
            }
            Back();
        }
        private void DeleteStudent(object StudentObject)
        {
            StudentViewModel Student = StudentObject as StudentViewModel;
            if (Student != null)
            {
                Students.Remove(Student);
            }
            Back();
        }
    }
}
