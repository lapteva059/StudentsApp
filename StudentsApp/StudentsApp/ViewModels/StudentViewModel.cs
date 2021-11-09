using System.ComponentModel;
using StudentsApp.Models;

namespace StudentsApp.ViewModels
{
    public class StudentViewModel : INotifyPropertyChanged
    {
        public event PropertyChangedEventHandler PropertyChanged;
        StudentsListViewModel lvm;

        public Student Student { get; private set; }

        public StudentViewModel()
        {
            Student = new Student();
        }

        public StudentsListViewModel ListViewModel
        {
            get { return lvm; }
            set
            {
                if (lvm != value)
                {
                    lvm = value;
                    OnPropertyChanged("ListViewModel");
                }
            }
        }
        public string Name
        {
            get { return Student.Name; }
            set
            {
                if (Student.Name != value)
                {
                    Student.Name = value;
                    OnPropertyChanged("Name");
                }
            }
        }
        public string StudentIDNumber
        {
            get { return Student.StudentIDNumber; }
            set
            {
                if (Student.StudentIDNumber != value)
                {
                    Student.StudentIDNumber = value;
                    OnPropertyChanged("StudentIDNumber");
                }
            }
        }
        public string GroupNumber
        {
            get { return Student.GroupNumber; }
            set
            {
                if (Student.GroupNumber != value)
                {
                    Student.GroupNumber = value;
                    OnPropertyChanged("GroupNumber");
                }
            }
        }

        public string YearOfAdmission
        {
            get { return Student.YearOfAdmission; }
            set
            {
                if (Student.YearOfAdmission != value)
                {
                    Student.YearOfAdmission = value;
                    OnPropertyChanged("YearOfAdmission");
                }
            }
        }
        public string DateOfBirth
        {
            get { return Student.DateOfBirth; }
            set
            {
                if (Student.DateOfBirth != value)
                {
                    Student.DateOfBirth = value;
                    OnPropertyChanged("DateOfBirth");
                }
            }
        }
        public string Phone
        {
            get { return Student.Phone; }
            set
            {
                if (Student.Phone != value)
                {
                    Student.Phone = value;
                    OnPropertyChanged("Phone");
                }
            }
        }

        public bool IsValid
        {
            get
            {
                return ((!string.IsNullOrEmpty(Name.Trim())) ||
                    (!string.IsNullOrEmpty(StudentIDNumber.Trim())) ||
                    (!string.IsNullOrEmpty(GroupNumber.Trim())) ||
                    (!string.IsNullOrEmpty(YearOfAdmission.Trim())) ||
                    (!string.IsNullOrEmpty(DateOfBirth.Trim())) ||
                    (!string.IsNullOrEmpty(Phone.Trim())));
            }
        }
        protected void OnPropertyChanged(string propName)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(propName));
        }
    }
}
